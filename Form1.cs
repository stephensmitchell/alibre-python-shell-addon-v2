using System;
using System.Windows.Forms;
using AlibreX;

namespace AlibrePythonShell
{
    public partial class Form1 : Form
    {
        private readonly IADSession _rootIn;
        public Form1(IADSession _rootInv)
        {
            InitializeComponent();
            _rootIn = _rootInv;
        }

        private void elementHost1_ChildChanged(object sender, System.Windows.Forms.Integration.ChildChangedEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            var PythonShell = new MainWindow(_rootIn);
           PythonShell.Show();
        }
    }
}
