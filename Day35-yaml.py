import yaml
yaml_config = '''
server_deploy:
  hostname: Web-Prod-01
  os: Ubuntu-22.04
  network:
    ip: 10.0.0.5
    gateway: 10.0.0.1
    ports:
      - 80
      - 443
      - 22
'''
config = yaml.safe_load(yaml_config)
hn = config["server_deploy"]["hostname"]
ip = config["server_deploy"]["network"]["ip"]
ports = config["server_deploy"]["network"]["ports"]
for port in ports:
    print(f"【部署确认】即将上线服务器{hn},分配ip：{ip},请防火墙放行以下端口{port}")