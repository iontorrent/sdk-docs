import requests
import urlparse
import bs4


class ModelDocScraper:
    def __init__(self, ts_base_url, auth, target_app="rundb", pg_db_name="iondb"):

        admin_username, admin_password = auth

        self.target_app = target_app
        self.pg_db_name = pg_db_name

        #Assemble model listing url
        self.admin_docs_url = ts_base_url

        #Start a session to grab cookies
        self.requests_session = requests.Session()

        #Make a request to the model list page, returning the admin login page
        admin_login_page_request = self.requests_session.get(self.admin_docs_url)

        #Rasies an exception if http status code is not 200
        admin_login_page_request.raise_for_status()

        #Extract the csrfmiddlewaretoken from the login page and the cookies
        admin_login_soup = bs4.BeautifulSoup(admin_login_page_request.text)
        admin_csrfmiddlewaretoken = admin_login_soup.find("input", {"name": "csrfmiddlewaretoken"})['value']
        admin_next_suffix = admin_login_soup.find("input", {"name": "next"})['value']

        #Make a POST request to login using the csrf scraped from the login and the cookies from the initial request
        admin_login_request = self.requests_session.post(
            self.admin_docs_url,
            {
                "username": admin_username,
                "password": admin_password,
                "csrfmiddlewaretoken": admin_csrfmiddlewaretoken,
                "next": admin_next_suffix,
                "this_is_the_login_form": "1"
            })

        #Parse model doc listing page to locate the table for "target_app"
        admin_model_list_soup = bs4.BeautifulSoup(admin_login_request.text)
        admin_target_app_table_heading = admin_model_list_soup.find("h2", {"id": "app-%s" % target_app})

        if not admin_target_app_table_heading:
            raise ValueError("Could not find app:%s on model listing page." % target_app)

        #Scrape all links to model docs
        model_names = []
        model_links = []
        for admin_model_doc_link in admin_target_app_table_heading.findNext('table').findAll('a'):
            model_names += [admin_model_doc_link.text]
            model_links += [urlparse.urljoin(ts_base_url, admin_model_doc_link['href'])]

        self.models = zip(model_names, model_links)
        self.model_names = model_names

        print "Found %i model doc pages for %s..." % (len(model_names), target_app)

    def _fetch_single_model_docs_soup(self, model_url):

        single_model_docs_request = self.requests_session.get(model_url)

        #Rasies an exception if http status code is not 200
        single_model_docs_request.raise_for_status()

        #Parse model docs page
        single_model_docs_soup = bs4.BeautifulSoup(single_model_docs_request.text)
        model_table = single_model_docs_soup.find("table", {"class": "model"})

        #Remove links from foreign keys and do some basic styles
        model_table["border"] = "1"
        [fk_link.replaceWith(fk_link.text) for fk_link in model_table.findAll('a')]
        [p_el.replaceWith(p_el.text) for p_el in model_table.findAll('p')]
        for th_el in model_table.findAll('th'):
            th_el['style'] = "background: #C8D5E6;"

        #Remove django functions from model docs
        #Example: controlSeqKit_applProduct_set.all
        for model_field in model_table.findAll('tr'):
            for exclude_key in [".all", ".count", "natural_key"]:
                if exclude_key in model_field.text:
                    model_field.replaceWith("")

        #Remove custom functions from model docs
        #Example: get_flows
        for model_field in model_table.findAll('tr'):
            field_columns = list(model_field.findAll("td"))
            if len(field_columns) == 3:
                field_name, field_data_type, field_info = field_columns
                if field_data_type.text == "":
                    model_field.replaceWith("")

        #Add (ForeignKey) to related rows
        #Example: kitinfo (ForeignKey)
        for model_field in model_table.findAll('tr'):
            field_columns = list(model_field.findAll("td"))
            if len(field_columns) == 3:
                field_name, field_data_type, field_info = field_columns
                if field_data_type.text in self.model_names or field_data_type.text == "User":
                    field_data_type.string = field_data_type.text + " (ForeignKey)"

        return model_table

    def get_model_docs_html(self):
        for model_name, model_link in self.models:

            pg_db_name = self.pg_db_name
            pg_table_name = self.target_app + "_" + model_name.lower()

            model_docs_header = "<h2>%s Table</h2><p>Postgresql db: <strong>%s</strong><br>Postgresql table: <strong>%s</strong></p>\n<br>\n" \
                                % (model_name, pg_db_name, pg_table_name)

            model_docs_html = str(self._fetch_single_model_docs_soup(model_link))

            #Switch docs naming to more databaseish terms
            model_docs_html = model_docs_html.replace("object", "row")

            yield locals()

    def dump_model_docs_jive_html(self, path="build/model_docs_jive.html"):
        with open(path, "w") as jive_html_file:
            for model_name, model_link in self.models:

                pg_db_name = self.pg_db_name
                pg_table_name = self.target_app + "_" + model_name.lower()

                model_docs_header = "<h2>%s Table</h2><p>Postgresql db: <strong>%s</strong><br>Postgresql table: <strong>%s</strong></p>\n<br>\n" \
                                    % (model_name, pg_db_name, pg_table_name)

                model_docs_html = str(self._fetch_single_model_docs_soup(model_link))

                #Switch docs naming to more databaseish terms
                model_docs_html = model_docs_html.replace("object", "row")

                jive_html_file.write(model_docs_header)
                jive_html_file.write(model_docs_html)
                jive_html_file.write("<br>")


    def dump_model_docs_confluence_markup(self, path="build/model_docs_jive.html"):
        return
