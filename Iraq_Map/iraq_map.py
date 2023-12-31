import networkx as nx
import matplotlib.pyplot as plt

plt.figure(1,figsize=(50,50))


#===========================================================================================================================

graph={
        'Baghdad':[('Babel',80),('Wasit',160),('Diyala',90),('Salah_ad-Din',120),('Anbar',160)],
        
        'Basra':[('Maysan',100),('Dhi_Qar',70),('Motana',100)],
        
        'Najaf':[('Motana',100),('Qadisiyyah',100),('Karbala',80),('Anbar',130),('Babel',90)],
        
        'Karbala':[('Najaf',80),('Babel',80),('Anbar',130)],
        
        'Dhi_Qar':[('Maysan',100),('Basra',70),('Motana',100),('Qadisiyyah',100),('Wasit',120)],
        
        'Wasit':[('Maysan',120),('Dhi_Qar',120),('Qadisiyyah',100),('Babel',80),('Baghdad',160),('Diyala',150)],
        
        'Salah_ad-Din':[('Anbar',200),('Baghdad',120),('Diyala',90),('Kirkuk',100),('Nineveh',150),('Sulaymaniyah',200)],
        
        'Nineveh':[('Anbar',180),('Salah_ad-Din',150),('Erbil',100),('Duhok',300)],
        
        'Anbar':[('Najaf',130),('Karbala',130),('Babel',160),('Baghdad',160),('Salah_ad-Din',200),('Nineveh',180)],
        
        'Diyala':[('Wasit',150),('Baghdad',90),('Salah_ad-Din',90),('Sulaymaniyah',250)],
        
        'Kirkuk':[('Salah_ad-Din',100),('Sulaymaniyah',150),('Erbil',100)],
        
        'Sulaymaniyah':[('Diyala',250),('Kirkuk',150),('Erbil',100),('Salah_ad-Din',200)],
        
        'Erbil':[('Sulaymaniyah',100),('Kirkuk',100),('Nineveh',100),('Duhok',200)],
        
        'Duhok':[('Erbil',200),('Nineveh',300)],
        
        'Qadisiyyah':[('Najaf',100),('Motana',100),('Dhi_Qar',100),('Wasit',100),('Babel',80)],
        
        'Babel':[('Najaf',90),('Qadisiyyah',80),('Wasit',80),('Baghdad',80),('Anbar',160),('Karbala',80)],
        
        'Maysan':[('Dhi_Qar',100),('Wasit',120),('Basra',100)],
        
        'Motana':[('Basra',100),('Dhi_Qar',100),('Qadisiyyah',100),('Najaf',100)]
}

#===========================================================================================================================

h_table={   
    "Baghdad": 70,
    "Basra": 0,
    "Najaf": 80,
    "Karbala": 80,
    "Dhi_Qar": 100,
    "Wasit": 130,
    "Salah_ad-Din": 180,
    "Nineveh": 200,
    "Anbar": 230,
    "Diyala": 220,
    "Kirkuk": 210,
    "Sulaymaniyah": 330,
    "Erbil": 210,
    "Duhok": 340,
    "Qadisiyyah": 260,
    "Babel": 290,
    "Maysan": 130,
    "Motana": 192       
}

#===========================================================================================================================


P={
        'Baghdad': (16.9,15.8),
        'Basra': (23.9,7),
        'Najaf': (15,9.5),
        'Karbala': (15,13),
        'Dhi_Qar': (21.2,9.5),
        'Wasit': (19.9,14),
        'Salah_ad-Din': (14.3,19),
        'Nineveh': (11.2,23.8),
        'Anbar': (9.3,15.2),
        'Diyala': (18,17.5),
        'Kirkuk': (15.6,21.9),
        'Sulaymaniyah': (18.6,22.5),
        'Erbil': (15.8,24.8),
        'Duhok': (13.3,26.9),
        'Qadisiyyah': (18,11.5),
        'Babel': (16.8,13.8),
        'Maysan': (23.2,11.5),
        'Motana': (19,6.8)

}

#===========================================================================================================================

G = nx.DiGraph()
# Add nodes to the graph
for node in graph:
        G.add_node(node)
# Add edges with edge costs
for node, edges in graph.items():
        for neighbor, cost in edges:
                G.add_edge(node, neighbor, weight=cost)
                
                
                
label = nx.get_edge_attributes(G, 'weight')
                


plt.subplot(1,2,1)

plt.title("Iraq_Map")


node_colors = [
        "Red",
        "Green",
        "Blue",
        "Yellow",
        "Purple",
        "Orange",
        "Pink",
        "Brown",
        "Black",
        "Gray",
        "Cyan",
        "Magenta",
        "Lime",
        "Maroon",
        "Olive",
        "Teal",
        "Navy",
        "Silver"
]


#===========================================================================================================================

nx.draw_networkx(G,pos=P,with_labels=True,node_color=node_colors,node_size=500,font_color='white',font_size=4)

nx.draw_networkx_edge_labels(G,pos=P,edge_labels=label)

plt.show()

