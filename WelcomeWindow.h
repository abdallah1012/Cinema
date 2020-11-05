#ifndef WELCOMEWINDOW_H
#define WELCOMEWINDOW_H

#include <QWidget>
#include <QtWidgets>
using namespace std;

class WelcomeWindow : public QWidget
{
    Q_OBJECT
public:
    explicit WelcomeWindow(QWidget *parent = nullptr);

    QPushButton * sign_in;
    QLineEdit *username_entry;
    QLineEdit *password_entry;
    QGridLayout * grid;
    ~WelcomeWindow();
signals:
public slots: void SignInButton();

};

#endif // WELCOMEWINDOW_H
