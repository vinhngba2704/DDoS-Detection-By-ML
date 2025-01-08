# Block all traffic for retraining Model 

1. Prevent all IP forwarding
```
sudo iptables -A FORWARD -j DROP
```
2. Delete the rule
```
sudo iptables -D FORWARD -j DROP
```