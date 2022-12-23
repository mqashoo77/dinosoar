from django.shortcuts import render
from datetime import datetime

def show_dino(request, name):
    data = {
        "dinosaurs": [
            "Tyrannosaurus",
            "Stegosaurus",
            "Raptor",
            "Triceratops",
        ],
        "now": datetime.now(),
    }
    return render(request, name + ".html", data)
