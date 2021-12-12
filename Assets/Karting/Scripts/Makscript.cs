using UnityEngine;
using System.IO;
namespace MakVerse
{
    public class Makscript : MonoBehaviour
    {
        public TextAsset file;
        public float[] Mak69;
        private string arr;
        private void Start()
        {
            if (file)
            {
                arr = file.ToString();
                Debug.Log("I am getting data");
                Debug.Log(arr);
            }
        }
    }
}