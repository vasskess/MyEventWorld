from django.shortcuts import render


def error_400(request):
    return render(request, "error_400_template.html", status=400)


def error_403(request):
    return render(request, "error_403_template.html", status=403)


def error_404(request):
    return render(request, "error_404_template.html", status=404)


def server_errors(request):
    return render(request, "server_errors.html", status=500)
