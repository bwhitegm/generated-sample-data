This repository is just a backup/storage for all the resources that are currently available through our FHIR servers. The data
is stored in JSON transaction bundles and organized by type and fhir version.

If you want to insert this data into your server please consider using this tool: https://github.com/smart-on-fhir/tag-uploader.
You can read it's documentation for usage instructions, but the very basic example would be something like:

```sh
cd path/to/fhir-uploader
node . -d my/input/directory -S http://my.fhir/server
```
Just make sure that the `STU-3` directory is uploaded to stu3 server and the `DSTU-2` goes to dstu2 one.

For **XML** bundle files we have written another simple uploader tool: https://github.com/smart-on-fhir/xml-bundle-uploader


### Renewing patients
As time passes the patients get older. This may be an issue, especially for pediatric apps.
That is why the datasets must be periodically "renewed". To do so we have created a special
tool: https://github.com/smart-on-fhir/timeshift