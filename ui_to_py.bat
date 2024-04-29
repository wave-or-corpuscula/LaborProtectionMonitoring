@echo off

pyside6-uic app/forms/ui/AuthorizationFormUi.ui -o app/forms/authorization_form/AuthorizationUi.py
pyside6-uic app/forms/ui/MainMenuUi.ui -o app/forms/menu_form/MainMenuUi.py
pyside6-uic app/forms/ui/DataManagingUi.ui -o app/forms/data_managing_form/DataManagingUi.py
pyside6-uic app/forms/ui/BriefingsUi.ui -o app/forms/briefings_form/BriefingsUi.py