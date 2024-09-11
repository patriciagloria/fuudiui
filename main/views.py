from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi' : 'Fuudiui : Food di UI, Foodie UI!',
        'nama' : 'Patricia Gloria Sujatmoko Silaban',
        'npm': '2306275172'
    }

    return render(request, "main.html", context)