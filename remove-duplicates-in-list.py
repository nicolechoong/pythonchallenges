def minus_dupes(l):
    app = []
    for i in l:
        if i not in app:
            app.append(i)
    return app
