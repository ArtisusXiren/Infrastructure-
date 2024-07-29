To run task :
build an image of dataset in docker 
build an image of extraction in docker 
run dataset image first and then the extraction image
build the image using :
docker build -t xyzname .
we need to make a copy of csv file in the main system after running docker file for Dataset
this can be done by:
docker cp <container name>:/path/file_name .
container name is given after running the docker file

To run test:
build an image of test by accesing the test folder through cd test
run the test image 
you can build your own test cases by adding more values to orders list 
after adding values , be sure to assertion rules . 
Monthy revenue would have n in assertionequals as n in test case
in given test case there are 3 distinct dates , therefore 3 is kept in assertEqual call
similary for product_revenue , customer_revenue and top_customers(for these two the  values would be same)

note: if dockerfile has a different name than default , then syntax is :
docker build -t <tagname> -f <filename>