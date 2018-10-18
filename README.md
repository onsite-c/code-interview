# API docs

This API serves groups and their members. Groups may be nested.

## Resources


| endpoint  | description  |
|---|---|
|/groups   | list all groups  |
|/groups/<group_name>  | get a specific group  |
|/groups/<group_name>/members  | get the members of a group |

e.g. to fetch members of a group named "admins"

    $ curl -H "Authorization: Bearer $token" localhost:5000/groups/admins/members
    [
      {
        "name": "alex"
      },
      {
        "name": "tristan"
      }
    ]

Endpoints return 200 codes on success. When requesting information about a
group that does not exist, a 404 code is returned.

## Endpoint

http://localhost:5000

## Authentication

Endpoints require authentication. Provide the `Authorization` header with the
bearer token printed at server startup. For example:

    $ curl -H "Authorization: Bearer a6njk09m7fr61bp3tcoidsbj" localhost:5000/groups
