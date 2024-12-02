import numpy as np
import matplotlib.pyplot as plt
# Define parameters with integer RTT values
rtt = np.arange(0, 21, 1)  # Simulated RTTs from 0 to 20 (inclusive), only integers
cwnd = []  # To store congestion window values
threshold = 8  # cwnd threshold for transitioning to additive increase
additive_step = 1  # Additive increase step size

# Simulate TCP Reno behavior
current_cwnd = 1  # Start with cwnd=1
for t in rtt:
    if current_cwnd < threshold:
        current_cwnd *= 2  # Slow start (exponential growth)
    else:
        current_cwnd += additive_step  # Additive increase
    cwnd.append(current_cwnd)

# Plotting with limited RTT range
plt.figure(figsize=(8, 5))
plt.plot(rtt, cwnd, label="TCP Reno cwnd", color="blue", marker="o")
plt.axhline(y=threshold, color="red", linestyle="--", label="Threshold (Slow Start Limit)")
plt.xlabel("Round Trip Time (RTT)")
plt.ylabel("Congestion Window (cwnd)")
plt.title("TCP Reno - part 2")
plt.legend()
plt.show()

# Parameters for simulation with packet losses
loss_events = [8, 16]  # RTTs at which packet losses occur
cwnd = []  # To store congestion window values
current_cwnd = 1  # Start with cwnd=1

# Simulate TCP Reno with multiplicative decreases due to packet loss
for t in rtt:
    if t in loss_events:
        current_cwnd = max(1, current_cwnd // 2)  # Multiplicative decrease (halving cwnd)
    elif current_cwnd < threshold and t<5:
        current_cwnd *= 2  # Slow start (exponential growth)
    else:
        current_cwnd += additive_step  # Additive increase
    cwnd.append(current_cwnd)

# Plotting with packet loss events
plt.figure(figsize=(10, 6))
plt.plot(rtt, cwnd, label="TCP Reno cwnd", color="blue", marker="o")
plt.axhline(y=threshold, color="red", linestyle="--", label="Threshold (Slow Start Limit)")
for loss in loss_events:
    plt.axvline(x=loss, color="purple", linestyle="--", label="Packet Loss")
plt.xlabel("Round Trip Time (RTT)")
plt.ylabel("Congestion Window (cwnd)")
plt.title("TCP Reno: cwnd vs RTT with Packet Loss Events")
plt.legend()
plt.grid()
plt.show()