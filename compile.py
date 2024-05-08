from os import system

system('mustache data.json science.mustache.html > science.html')
system('mustache data.json work_studies.mustache.html > work_studies.html')
system('mustache data.json contactme.mustache.html > contactme.html')