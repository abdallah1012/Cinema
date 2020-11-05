#include "MainMenu.h"

MainMenu::MainMenu(MainMenu::UserPrivileges privilege, string username)
{
    if (privilege==MainMenu::STUDENT){
        //call student constructor
        //load student recommendations
    }
    else{
        //call professor constructor
    }
    this->show();
}

Mainmenu::~MainMenu() {}
