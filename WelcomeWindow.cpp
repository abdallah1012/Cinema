#include "WelcomeWindow.h"
#include "User.h"

WelcomeWindow::WelcomeWindow(QWidget *parent) : QWidget(parent)
{
    sign_in = new QPushButton("Sign In");

    username_entry = new QLineEdit();
    username_entry->setPlaceholderText("username");

    password_entry = new QLineEdit();
    password_entry->setPlaceholderText("password");
    password_entry->setEchoMode(QLineEdit::Password);

    grid = new QGridLayout();
    grid->addWidget(username_entry);
    grid->addWidget(password_entry);
    grid->addWidget(sign_in);

    this->setLayout(grid);
    QObject::connect(sign_in,SIGNAL(clicked()),this,SLOT(SignInButton()));

}
void WelcomeWindow::SignInButton(){
    User::SignIn(username_entry->text().toStdString(),
                 password_entry->text().toStdString());

}

WelcomeWindow::~WelcomeWindow(){
    delete sign_in;
    delete username_entry;
    delete password_entry;
    delete grid;
}
