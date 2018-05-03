# splash-resolver
This project, provides an AWS based service to easily discover in which database a splash exists

to utilize the service, please utilize the following temporary links. We will provide a complete api in the
next couple of days. Please be aware that we are throtteling the system to 1 request per second right now. If you get throttled, you will receive
a 429 error code.

# api

This section describes the basic API

*  POST - https://api.metabolomics.us/splash/resolve

This request will create a new entry and requires a well formated json object, looking like this:

{

 "inchiKey" : "the inchi key",

 "splash" : "the splash",

 "origin" : "the origin of this spectra, like massbank or nist"

 "record" : "the official public address in form of an url of the spectra"

}

*  GET - https://api.metabolomics.us/splash/resolve/{id}

returns the complete record of the given id

*  GET - https://api.metabolomics.us/splash/resolve

list the content of the database

*  GET - https://api.metabolomics.us/splash/resolve/{inchiKey}

lists all records associated with this InChI Key

*  GET - https://i1bicedwnd.execute-api.us-east-1.amazonaws.com/dev/resolve/inchiKey/{splash}

lists all records associated with the splash

# deployment

to deploy the application to the configured AWS account, please modify the domain settings in the serverless file and than execute

```
sls deploy
```

or 

```
sls deploy --stage prod
```

to select your preffered stage
