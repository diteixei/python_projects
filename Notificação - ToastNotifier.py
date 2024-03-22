from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast(
    "Notificação",
    "Olá Diego :)",
    threaded=True,
    icon_path=None,
    duration=3

)