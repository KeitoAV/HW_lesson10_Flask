import foo

from flask import Flask

app = Flask(__name__)  # экземпляр Flask


def main():
    @app.route("/")
    def read_candidates():
        """Выводим данные всех кандидатов """
        read_page = foo.load_page()

        return read_page

    @app.route("/candidates/<int:x>")
    def read_candidate(x):
        """Выводим 'img' и данные одного кандидата по id"""
        if foo.get_id(x) is True:
            read_link = foo.get_img(x)
        else:
            read_link = 'Такого кандидата у нас нет.'
        return read_link

    @app.route("/skills/<x>")
    def read_candidate_skill(x):
        """Выводим кандидатов у которых есть 'skills'"""
        if foo.get_skills(x) is True:
            read_skill = foo.get_skill(x)
        else:
            read_skill = 'Кандидаты такой специальностью не владеют'

        return read_skill

    app.run()


if __name__ == '__main__':
    main()
