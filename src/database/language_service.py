from database.models.language import Language
from models.code_language import LanguageStorable, CodeLanguage
import database.manager as db_manager


class Actions:

    @staticmethod
    def get_languages_for_repo(repo_id: int) -> [Language]:
        if isinstance(repo_id, int):
            session = db_manager.get_session()
            languages = session.query(Language).filter(Language.repo_id == repo_id).one_or_none()
            return languages
        else:
            raise ValueError

    @staticmethod
    def insert_new_language(language: LanguageStorable):
        if isinstance(language, CodeLanguage):
            try:
                language_db_object = Actions._map_language_to_orm_object(language)
                if language_db_object:
                    session = db_manager.get_session()
                    session.add(language_db_object)
                    session.commit()
            except AttributeError as e:
                print("Unable to save Language Object - missing required attributes: {}".format(e))

    @staticmethod
    def _map_language_to_orm_object(language: CodeLanguage) -> Language:
        if language.id and language.name:
            language_orm = Language(name=language.name, id=language.id,
                                    textColor=language.textColor)
            return language_orm
        else:
            raise AttributeError

    @staticmethod
    def get_all_languages():
        session = db_manager.get_session()
        return session.query(Language).all()
