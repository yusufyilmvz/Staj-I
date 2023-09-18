using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Python.Runtime;

namespace Yusuf_Yılmaz_Staj_PythonNet
{
    public class Program
    {
        static void Main(string[] args)
        {
            PythonDosyasiniCalistir("yusuf_yilmaz_python");
        }

        static void PythonDosyasiniCalistir(string dosyaIsmi)
        {
            Runtime.PythonDLL = "python311.dll";
            //PythonEngine.BeginAllowThreads();
            PythonEngine.Initialize();
            using (Py.GIL())
            {
                dynamic pythonDosyasi = Py.Import(dosyaIsmi);
                var sonuc = pythonDosyasi.InvokeMethod("veritabani_mesajlar_al");
                foreach (var element in sonuc)
                {
                    Console.WriteLine(element.ToString());
                }
                //Console.WriteLine(sonuc);
                Console.ReadLine();
            }
        }
    }
}
