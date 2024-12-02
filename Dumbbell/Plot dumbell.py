import pandas as pd
import matplotlib.pyplot as plt

#Part 3 - dumbbell architecture (lossless)
def plotExperiment(tcptype, loss):       
    if loss:
        workDir = "Dumbbell\\Loss results"
    else:    
        workDir = "Dumbbell\\Lossless results"

    df_5 = pd.read_csv(workDir+"\\cwnd_5_"+tcptype+".csv")
    df_10 = pd.read_csv(workDir+"\\cwnd_10_"+tcptype+".csv")
    df_35 = pd.read_csv(workDir+"\\cwnd_35_"+tcptype+".csv")
    df_100 = pd.read_csv(workDir+"\\cwnd_100_"+tcptype+".csv")

    plt.figure()
    plt.plot(df_5['Timestamp'],df_5['CWND'])
    plt.plot(df_10['Timestamp'],df_10['CWND'])
    plt.plot(df_35['Timestamp'],df_35['CWND'])
    plt.plot(df_100['Timestamp'],df_100['CWND'])

    if loss:
        plt.title("S1 CWND - " + tcptype + " (Loss)")
    else:
        plt.title("S1 CWND - " + tcptype + " (Lossless)")
    
    plt.legend(["n=5","n=10","n=35","n=100"])
    plt.xlabel("Time")
    plt.ylabel("CWND")
    plt.xlim(left=0,right=60)
    
#Reno
tcptype = "reno"
plotExperiment(tcptype,loss=False)
plt.savefig("Figures\\Reno (lossless).png")

#New Vegas
tcptype = "vegas"
plotExperiment(tcptype,loss=False)
plt.savefig("Figures\\Vegas (lossless).png")

#Cubic
tcptype = "cubic"
plotExperiment(tcptype,loss=False)
plt.savefig("Figures\\Cubic (lossless).png")

plt.show()

#Part 4 - dumbbell architecture (1% packet loss)
#Reno
tcptype = "reno"
plotExperiment(tcptype,loss=True)
plt.savefig("Figures\\Reno (loss).png")

#New Vegas
tcptype = "vegas"
plotExperiment(tcptype,loss=True)
plt.savefig("Figures\\Vegas (loss).png")

#Cubic
tcptype = "cubic"
plotExperiment(tcptype,loss=True)
plt.savefig("Figures\\cubic (loss).png")

plt.show()

#Part 5 - dumbell architecture (BBR policy)
tcptype = "bbr"
plotExperiment(tcptype,loss=False)
plt.savefig("Figures\\BBR (lossless).png")
plotExperiment(tcptype,loss=True)
plt.savefig("Figures\\BBR (loss).png")

plt.show()