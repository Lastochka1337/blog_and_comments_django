import django_setup

from managmet.models import Post, Commentary

while True:
    a = input("1 - Створити новий пост\n2 - Додати коментар до посту\n3 - Редагувати текст посту\n4 - Вихід з програми")
    match a:
        case "1":
            name = input("Name: ")
            content = input("Content: ")
            publication_date = input("Publication date (YYYY-MM-DD): ")
            Post(name = name, content = content, publication_date = publication_date).save()
        case "2":
            post_id = int(input("Post ID: "))
            text = input("Text: ")
            author = input("Author: ")
            creation_date = input("Creation Date (YYYY-MM-DD): ")
            Commentary(text = text, author = author, creation_date = creation_date).save()
            comment = Commentary.objects.all()
            post = Post.objects.get(id = post_id)
            post.comments.add(comment.last())
        case "3":
            post_id = int(input("Post ID: "))
            post = Post.objects.get(id = post_id)
            post.content = input("New content: ")
            post.save()
        case "4":
            break