# API docs

This API serves groups and their members.

To access and modify resources, you can use any HTTP method
GET POST PUT PATCH DELETE OPTIONS

## Resources


| endpoint  | notes  |
|---|---|
|/group   | list all groups  |
|/group/<group_name>  | lookup specific group  |
|/group/<group_name>/member  | members of group named "group_name"  |

e.g. to fetch members of a group named "admins"

```
$ curl localhost:8080/group/admins/member
[
  {
    "id": "2",
    "groupId": "admins",
    "members": [
      "alex",
      "tristan"
    ]
  }
]
```

## Endpoint

http://localhost:8080

## Return code

* API returns HTTP 200, even when a resource is not found.
* Incase of non-existent resource, response is empty array i.e. `[]` or object with no properties i.e. `{}`

e.g.
```
$ curl localhost:8080/group/NON_EXISTENT_GROUP
{}

$ curl localhost:8080/group/NON_EXISTENT_GROUP/member
[]

$ curl localhost:8080/NON_EXISTENT_RESOURCE
{}
```
