#ifndef MAINMENU_H
#define MAINMENU_H
#include <QWidget>
#include <string>
using namespace std;

class MainMenu : public QWidget
{
    Q_OBJECT
public:
    enum UserPrivileges{STUDENT,PROFESSOR};
    MainMenu(MainMenu::UserPrivileges privilege,string username);
    ~MainMenu();
signals:

};

#endif // MAINMENU_H
