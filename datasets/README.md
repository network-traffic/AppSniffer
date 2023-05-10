# AppSniffer datasets

The datasets used for the AppSniffer Experiment consist of five types:

**Android150_without_VPN**


**Android150_with_SuperVPN**


**Android150_with_NordVPN**


**Android150_with_TurboVPN**


**Android150_with_Surfshark**

We provide three formats of each dataset (raw pcap files, pickle files, and CSV files) for future research work. 

In our experiments, we extract flow data from pcap files and generate CSV files of packet length sequence features.

(Pcap files -> Pickle files -> CSV files)

From pcap files to pickle files, we use the FlowPrint library with --pcaps options.

https://flowprint.readthedocs.io/en/latest/usage/command_line.html

python3 -m flowprint --pcaps <data.pcap> --write <flows.p>




## Bibtex
```
@inproceedings{vanede2020flowprint,
  title={{FlowPrint: Semi-Supervised Mobile-App Fingerprinting on Encrypted Network Traffic}},
  author={van Ede, Thijs and Bortolameotti, Riccardo and Continella, Andrea and Ren, Jingjing and Dubois, Daniel J. and Lindorfer, Martina and Choffness, David and van Steen, Maarten, and Peter, Andreas},
  booktitle={NDSS},
  year={2020},
  organization={The Internet Society}
}
```
