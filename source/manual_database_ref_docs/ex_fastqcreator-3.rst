Fastq Creator 'bam2fastq' Method
================================

.. code-block:: python

	def bam2fastq(self, bam_filename_list, fastq_filename):
		try:
			with open(fastq_filename, 'w') as fastq_file:

				for bam_file in bam_filename_list:
					if os.path.exists(bam_file):
						try:
							samfile = pysam.Samfile(bam_file, mode="rb",check_header=False,check_sq=False)
							for x in samfile.fetch(until_eof=True):
								if x.is_reverse:
									qual = x.qual[::-1]
									seq = reverse_complement(x.seq)
								else:
									qual = x.qual
									seq = x.seq
								fastq_file.write("@%s\n%s\n+\n%s\n" % (x.qname,seq,qual))
							samfile.close()
						except:
							traceback.print_exc()
		except:
			traceback.print_exc()

Like the bam2fastq_picard method, it takes a list of bam filenames and a fastq filename.

It opens the fastq file for writing, calls pysam.Samfile on each bam filename, and writes the results directly to the fastq file.
