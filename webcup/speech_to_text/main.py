import face_recognition

known_image = face_recognition.load_image_file("donald.jpeg")
unknown_image = face_recognition.load_image_file("Joe-Biden.jpg")

encoded_known_image = face_recognition.face_encodings(known_image)[0]
encoded_unknown_image = face_recognition.face_encodings(unknown_image)[0]


results = face_recognition.compare_faces([encoded_known_image],encoded_unknown_image)

print(results)