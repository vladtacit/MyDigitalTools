# Install and configure Grafana

[Install Grafana on Debian or Ubuntu](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/)

[Установка Grafana в Debian](https://rtfm.wiki/linux/grafana/grafana_install)

[Grafana Labs update regarding CircleCI security updates](https://grafana.com/blog/2023/01/12/grafana-labs-update-regarding-circleci-security-updates/)

1. The prerequisite packages:
   * apt-transport-https
   * software-properties-common
   * wget

Check package version:

```bash
$ apt list -a apt-transport-https
Listing... Done
apt-transport-https/stable,now 2.6.1 all [installed]

$ apt list -a software-properties-common
Listing... Done
software-properties-common/stable,now 0.99.30-4.1~deb12u1 all [installed,automatic]

$ apt list -a wget
Listing... Done
wget/stable,now 1.21.3-1+b2 amd64 [installed]
```

2. Import the GPG key (**Need VPN!!!**):

```bash
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null
gpg: no valid OpenPGP data found.
```

```bash
wget -q -O /usr/share/keyrings/grafana.key https://apt.grafana.com/gpg.key
```

```bash
wget -q -O /etc/apt/keyrings/grafana.key https://apt.grafana.com/gpg.key
```

&#9635;
