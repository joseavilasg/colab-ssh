import re


def get_argo_tunnel_config(initial_path=""):
  hostname = None
  with open(initial_path+"cloudflared.log", "r", encoding="utf-8") as f:
    output = "".join(f.readlines())
  results = re.findall(
      ':\"\| *https://(.+?.trycloudflare.com) *\|\"}', output)

  if not results:
    raise Exception(
        "Cannot get any result from cloudflared metrics")
  hostname = results[-1]
  if hostname is None:
    raise Exception(
        "Cannot get the hostname from cloudflared, it looks like the connection has failed.")
  return {
      "domain": hostname.strip(),
      "protocol": "",
      "port": 22
  }
