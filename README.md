# CalendaApi
A Quick Booking System Using CC [Country Code] and Time offset

## Requirements
<p>You must have atleast python2 or python3 installed on your enviroment / server</p>
<p>Make sure you have no software blocking common ports. :8080, :80, :443 otherwise chnage port manual<p>

## Dependencies
>FastAPI was used to enable and fasten my fancy url mechanism and JSON responses<p>
>Uvicorn server was also used for transporting our main app through any available port. :8080 but can be changed based on server requirement.

## Installations
>Install dependencies <br>
>`pip3 install -r requirements.txt`

>Start server <br>
>`uvicorn main:app --reload`
  
>Option config
  >`You can activate your venv: source venv/bin/activate`

## EndPoints
>Entry point <br>
>`host:8080/`

>Fetch Holidays By [Country Code] <br>
>`host:8080/get-holidays/ng`

>Post request with array object[from_, to_, cc_] see sample below<br>
>`host:8080/get-meeting`

>Request perfect date/time dynamically using the below format <br>
`Sample post data: `
<pre><code>{
    "data": [
        {
            "from_": "2022-05-02T09:00:00.0+08:00",
            "to_": "2022-05-02T17:00:00.0+08:00",
            "cc_": "SG"
        },
        {
            "from_": "2022-05-02T09:00:00.0+01:00",
            "to_": "2022-05-02T17:00:00.0+01:00",
            "cc_": "NG"
        },
        {
            "from_": "2022-05-02T09:00:00.0+05:30",
            "to_": "2022-05-02T17:00:00.0+05:30",
            "cc_": "IN"
        }
    ]
  }</code></pre>

<br>

  Note<br>
  API docker added but has not been tested on any container: application run fine, no database required

<!-- Badges -->
## Technologies
<p>

![JavaScript](https://img.shields.io/badge/-JSON-black?style=flat-square&logo=json)
![Nodejs](https://img.shields.io/badge/RESTAPI-INCLUDED-blue)
![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)

</p>

## My Social Links
![GitHub followers](https://img.shields.io/github/followers/nusktec?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/revelation_rsc?style=social)
