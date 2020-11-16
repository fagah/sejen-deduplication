# sejen-deduplication
Using this simple machine learning techniques for identity de-duplication based on biographic data.

## Who is this resource for?
This resource is useful to deduplicate identity based on simple biographic data such as name, gender, address and birthdate. The particularity of this solution is that for the deduplication to work, the fields do not need to have an exact match between entities and values can be missing. The solution also makes use of simple machine learning techniques for the deduplication.
Use this resource to anyone who is looking for a simple option to deduplicate digital records such as patient or enrollment records when the data is not completely clean.
## Who owns and updates this resource?
This resource was originally created by *SEJEN CI*. The code used for this project is available in a Github repository that can be reached here: https://github.com/fagah/sejen-deduplication .

For questions, ideas or comments, please contact info@sejen.ci

## When has this resource been used?
This resource has been implemented by SEJEN CI for the the Ministry of Health in Cote D’Ivoire, with funding by PEPFAR and MCC. The scope of implementation covers the HIV/AIDS patient population of a local PEPFAR implementation partner with community-based health-care facilities spread across Cote d’Ivoire. 

This resource was applied to the database of patient records of two large health units of the local implementation partner. The goal was to obtain hard statistics about the duplication of identity problem that was still just a hypothesis. The analysis proved that the duplication was real and led to the launching of a new project for the unique identification of patients for the entire network of PEPFAR implementation partners in Cote d’Ivoire. 
Note: Information about the unique patient identification project can be found her: [Link will be posted soon]

This solution directly contributes to solving the problem of duplicated identities in the Electronic Health-care Record system (SIGDEP2) used by the health-care units and administered by the Ministry of Health in Cote d’Ivoire. Prior studies have revealed that the duplication of identities exists both within the health-care units themselves and across the network. In other words, an individual may be found more than once within the patient’s registry at a given health care unit. That same individual may also be found more than once across multiple health care units. 

This duplication of identities can cause significant errors with the country HIV/AIDS statistics and can reduce the effectiveness of the overall program to fight against this pandemic.

## What intangible assets are needed?
Access and dealing with real patient records requires proper and secured handling of the data to maintain the privacy of the patients. This is particularly true of this data since identifying information is part of the data sets.

## Are the costs worth the while?
The cost of this solution is negligeable as the tools (Python and machine learning libraries) are all open source and the techniques on how to use the python code is accessible to any developer with reasonable Python coding skills.

## How do I get started?
First, review the characteristics of the data that was used by this resource. You may note similarities with your own program data. In the example for this resource we use common demographic fields such as: Family Name, Given Name, Phone Number, Birth Date and Gender. With this kind of data, you will often find that small errors are introduced during data entry. Therefore, an exact match on all the fields is then not possible to determine whether two records are duplicated.  

You can find a small sample of representative data which demonstrates these inperfections here: XXXXXXXXX 

Second, consult the simple Python source code that uses machine learning techniques to deduplicate the data. A small sample data set is provided to exercise the code.

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

For more informationm consult the excellent site https://dedupe.io/

