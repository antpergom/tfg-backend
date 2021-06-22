<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://imgur.com/xCreGFW.png" alt="Project logo"></a>
</p>

<h3 align="center">HeartSAC</h3>

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p > 
    <br> HeartSAC is a container-based system that captures real time heart data that is sent via HTTP and displays it in different functional ways through Grafana.
</p>


## 👓 About <a name = "about"></a>

This project is a simple system that was developed in order to get to know different technologies that caught our attention, such as Docker or Grafana.<br>
With this cotainer-based system you will be able to store inside the database heart rate and blood pressure just by doing HTTP requests. The data stored will be shown on Grafana, which can be easily customized to display it in every way possible. <br>
Despite being designed for heart measures, by changing some lines it can be used to manage and visualize every data you can think of.

## 🔧 Install

If you just want to use it as we built it, you'd just have to follow this steps:<br><br>
1.- Run docker-compose up<br>
2.- Go to localhost:3000 and log into Grafana with admin/admin<br>
3.- Go to Data Sources and configure InfluxDB. Set URL as "http://influxdb:8086", database as "influx" and user/password as "admin"/"admin"<br>
4.- To see if it worked, go to the Grafana explorer and try to do a search. You can put new data by using cURL to "{telegraf_IP}:8080/telegraf with a well-formatted JSON (example in the "Useful Commands.txt" file).<br>

On the other hand, if you want to customize this project you'd need to change the following aspects before making the previous steps:<br><br>

- Change the HTTP_listener plugin options inside the telegraf.conf file. "name_override" indicates the name of the measure, and with "tag_key" you can indicate the key that will let you filter measures
- There's nothing else really that you'd need to change, but if you insist in changing parameters such as the listening port, just google what you need, since both the docker-compose and telegraf.conf files have too many parameters to explain all of them.

## ✨ Usage <a name="usage"></a>

After finishing the installation process, you can use whenever you want the Grafana explorar, but because it is tedious, you can create dashboards to have prefixed measures the way you want. Since dashboards have too many options I will not explain here how to configure them, so I suggest you to look how to use them in the [official website](https://grafana.com/docs/grafana/latest/dashboards/)

## ✍️ Authors <a name = "authors"></a>

- [@alealclag](https://github.com/alealclag)
- [@antpergom](https://github.com/antpergom)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- At last, we want to thank [@bcremer](https://github.com/brcmer), from whom we took the Docker-compose file
