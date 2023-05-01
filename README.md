

- You should execute `build-image.sh` script everytime when you changed something in `superset_config.py`
- You should execute `first-build-superset.sh` script only if it's the first time you are setting up the Superset on your environment
- You can execute `build-superset.sh` script when you want to run Superset on your environment
  - You had to executed the `first-build-superset.sh` before execute this
- We can override Superset config variables in `superset_config` file which is located in this repo. Then, `Dockerfile` copy this file into `/app/` . If we set SUPERSET_CONFIG_PATH variable (we did in `Dockerfile`), CONFIG_PATH_ENV_VAR will be created while runtime and we will be able to override the configure variables [https://github.com/apache/superset/blob/master/superset/config.py#L1351]



# Essential Scripts to Run Superset

```bash
sudo docker run -d -p 8080:8088 --name superset apache/superset
```

 
```bash
sudo docker exec -it superset superset fab create-admin \
               --username admin \
               --firstname Superset \
               --lastname Admin \
               --email admin@superset.com \
               --password admin
```

```bash
sudo docker exec -it superset superset db upgrade
```


```bash
sudo docker exec -it superset superset load_examples
```


```bash
sudo docker exec -it superset superset init
```

# Setting for Public Access

If we want to configure Superset to public access, we need set a default role for not authenticated users in `superset_config.py`.

```python
PUBLIC_ROLE_LIKE = 'Gamma' # We can set our custom role
```

Then we have to re initialize Superset.

```bash
docker exec superset superset init
```

We can visit Superset's [official documentation](https://superset.apache.org/docs/security/) for more detail.
