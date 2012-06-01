deploy:
	echo 'CREATE DATABASE IF NOT EXISTS cpp_backend2;' | mysql -u root --password=rootpassword
	python manage.py syncdb
