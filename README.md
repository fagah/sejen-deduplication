# Deduplication of records based on biographic data
Use these simple machine learning techniques for identity de-duplication based on biographic data.

This sample code shows how to deduplicate identity-based on simple biographic data such as name, gender, address, and birthdate. The particularity of this solution is that for the deduplication to work, the fields do not need to have an exact match between entities and, also, values can be missing. This solution makes use of simple machine learning techniques for deduplication.

 *SEJEN CI* created this sample code. SEJEN CI is an analytical, research, and technology consulting company based in Abidjan, Côte d’Ivoire, which offers a range of high-quality consulting and analytical services to public and private SEJEN CI sector entities.  

For questions, ideas or comments, please contact info@sejen.ci

## What is the history behind this sample code?
A similar approach has been implemented by SEJEN CI for the Ministry of Health in Cote D’Ivoire, with funding by the US President's Emergency Plan For AIDS Relief (PEPFAR) and the Millenium Challenge Corporation (MCC). The implementation scope covered the HIV/AIDS patient population of a local PEPFAR implementation partner with community-based health-care facilities spread across Cote d’Ivoire.  

This deduplication solution was applied to the database of patient records of the local implementation partner's two large health units. The goal was to obtain hard statistics about the duplication of identity problem that was still just a hypothesis. 

## How do I get started?
First, review the characteristics of the data that was used by this resource. You may note similarities with your own program data. In the example for this resource we use common demographic fields such as: *Family Name, Given Name, Phone Number, Birth Date and Gender*. With this kind of data, you will often find that small errors are introduced during data entry. Therefore, an exact match on all the fields is not possible to determine whether two records are duplicated.  

You can find a small sample of representative data which demonstrates these inperfections in the file *csv_small_biographic_dataset.csv* 

Second, consult the simple Python source code that uses machine learning techniques to deduplicate the data. By default, this python code uses the small data sample provided.

## How do you run the script?

First ensure that you have Python 3 installed on your machine. This script has only been tested with Python 3.6.x but may work with previous versions. 

You can download python for your operatin system from this web site: https://www.python.org/downloads/

Then follow the steps below:

## Clone this repository using git

Clone the repo and navigate to it

<pre>
  git clone https://github.com/fagah/sejen-deduplication.git
  cd sejen-deduplication/
</pre>

## Installing virtualenv (this should need to be done only once)

<a href="https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/">virtualenv</a> is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.

<pre>
  python3 -m pip install --user virtualenv
</pre>

## Create the virtual environment (this should need to be done only once)
<pre>
  python3 -m venv env
</pre>

## Activate the virtual environment (this should be done EVERY TIME before running the code that follows

Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH:

<pre>
  source env/bin/activate
</pre>

## Installing packages

Now that you’re in your virtual environment you can install the necessary packages/libraries. Let’s install the Requests library from the Python Package Index (PyPI):

<pre>
  pip install -r requirements.txt
</pre>

## Dedupe records
You can now run the example deduplication code:
<pre>
  python3 csv_example.py
</pre>

This python code will create an interactive shell to ask you about potential duplicates. Use 'y' (yes), 'n' (no) and 'u' (unsure) keys to flag them, 'f' (finished) when you are finished. The data set is small, so just do 5 or 6 of these. 

In the end, this python code will generate a file called *csv_example_output.csv* that you can then inspect: 
- Open the file in Excel
- Sort the file on the field cluster_id

All the rows with the same cluster id are duplicates that the python library dedupe found. YOu will likely notice a few duplicates that were not caught. That's because we need a more robust training set with more examples of duplicate records. 

For more information consult the excellent site https://dedupe.io/ from which we borrowed heavily. All the credit goes to the makers of this excellent open-source machine learning library!

