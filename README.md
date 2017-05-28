# DevProjects

A website for showcasing your projects

### Structure

* **/src** - Python Source Files for Backend
* **/static** - CSS/JS/Static HTML
* **/templates** - HTML Templates

### Deployment Instructions

1. Determined by web host ... TBD
2. Place the following in your servers cron
```
*/45 * * * * /path/to/python3 /path/to/update_repos.py
```
3. Verify the database file has been written /src/database/
4. ... etc