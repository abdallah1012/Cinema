#include  "WelcomeWindow.h"
#include <QApplication>

int main(int argc, char **argv)
{
    QApplication app (argc, argv);
    WelcomeWindow * welcome_window = new WelcomeWindow();//initialize first widget displayed
    welcome_window->show();
    return app.exec();
}
