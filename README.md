# sejen-deduplication
Using simple machine learning techniques for Identity de-duplication
# Who is this resource for?
This resource is useful to deduplicate identity based on simple biographic data such as name, gender, address and birthdate. The particularity of this solution is that for the deduplication to work, the fields do not need to have an exact match between entities and values can be missing. The solution also makes use of simple machine learning techniques for the deduplication.
Use this resource to anyone who is looking for a simple option to deduplicate digital records such as patient or enrollment records when the data is not completely clean.
# Who owns and updates this resource?
This resource was originally created by *SEJEN CI* and is also hosted online at the Data Collaborative for Local Impact (DCLI website). 
The code used for this project is available in a Github repository that can be reached here

For questions, ideas or comments, please contact info@sejen.ci

# When has this resource been used?
This resource has been implemented by SEJEN CI for the the Ministry of Health in Cote D’Ivoire, with funding by PEPFAR and MCC. The scope of implementation covers the HIV/AIDS patient population of a local PEPFAR implementation partner with community-based health-care facilities spread across Cote d’Ivoire. 

This resource was applied to the database of patient records of two large health units of the local implementation partner. The goal was to obtain hard statistics about the duplication of identity problem that was still just a hypothesis. The analysis proved that the duplication was real and led to the launching of a new project for the unique identification of patients for the entire network of PEPFAR implementation partners in Cote d’Ivoire. 
Note: Information about the unique patient identification project can be found here.

This solution directly contribute to solving the problem of duplicated identities in the Electronic Health-care Record system (SIGDEP2) used by the health-care units and administered by the Ministry of Health in Cote d’Ivoire. Prior studies have revealed that the duplication of identities exists both within the health-care units themselves and across the network. In other words, an individual may be found more than once within the patient’s registry at a given health care unit. That same individual may also be found more than once across multiple health care units. 

This duplication of identities can cause significant errors with the country HIV/AIDS statistics and can reduce the effectiveness of the overall program to fight against this pandemic.

# What intangible assets are needed?
Access and dealing with real patient records requires proper and secured handling of the data to maintain the privacy of the patients. This is particularly true of this data since identifying information is part of the data sets.

# How do I get started?
First, jump right in by assimilating the context information that describes the characteristics of the network of health-care units in Cote d’Ivoire. You may note similarities with your own program of interest.

Second, review the characteristics of the data that was used by this resource. Once again, you may note similarities with your own program data.
Third, consult the simple Python source code that uses machine learning techniques to deduplicate the data. “Fake” test data is provided to exercise the code.

# Are the costs worth the while?
The cost of this solution is negligeable as the tools (Python and machine learning libraries) are all open source and the techniques on how to use the python code is accessible to any developer with reasonable Python coding skills.


# How to run the script ?

You have to add libraries to the mahcine which will run the script and launch it

# Installing virtualenv

<a href="https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/">virtualenv</a> is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.

<pre>
  python3 -m pip install --user virtualenv
</pre>

# Activating a virtual environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH

<pre>
source env/bin/activate
</pre>

# Installing packages

Now that you’re in your virtual environment you can install packages. Let’s install the Requests library from the Python Package Index (PyPI):

<pre>
pip install dedupe
</pre>

<pre>
pip install future
</pre>


<pre>
pip install unidecode
</pre>

# Run the script
python dedupecode.py
