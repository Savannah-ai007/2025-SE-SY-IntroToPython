def faces():
    faces = input()

    if "hello :)" in faces:
        newfaces = faces.replace(":)", "🙂")
    if "Goodbye :(" in faces:
        newfaces = newfaces.replace(":(", "🙁")

    print(newfaces)


faces()
