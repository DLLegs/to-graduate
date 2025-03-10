using System;
using System.Security.Cryptography;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void SignInButton_Click(object sender, EventArgs e)
        {
            string userId = id.Text;
            string userPassword = password.Text;

            if (userId.Equals("MyId") && userPassword.Equals("MyPassword"))
            {
                MessageBox.Show("로그인에 성공하였습니다.", "로그인");
            }
            else
            {
                MessageBox.Show("로그인에 실패하였습니다.", "로그인");
            }
        }

        private void password_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
