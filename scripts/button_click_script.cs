using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using System.Net;
using System.IO;

public class button_click_script : MonoBehaviour
{
    //public MeshRenderer MyRenderer;
    public Material red;
    public Material green;
    public string swap;

    public GameObject obj1;
    public GameObject obj2;

    //public string url = "http://192.168.1.103:5000";

    
    public void color_change()
    {
        string output;

        HttpWebRequest request = (HttpWebRequest)WebRequest.Create("http://192.168.43.156:5000/data");
        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        using (StreamReader streamReader = new StreamReader(response.GetResponseStream()))
        {
            output = streamReader.ReadToEnd();
        }

        Debug.Log(output);







        if (output == "left")
        {
            MeshRenderer meshRenderer1 = obj1.GetComponent<MeshRenderer>();
            meshRenderer1.material = red;

            MeshRenderer meshRenderer2 = obj2.GetComponent<MeshRenderer>();
            meshRenderer2.material = green;
        }
        else if(output == "right")
        {
            MeshRenderer meshRenderer1 = obj1.GetComponent<MeshRenderer>();
            meshRenderer1.material = green;

            MeshRenderer meshRenderer2 = obj2.GetComponent<MeshRenderer>();
            meshRenderer2.material = red;
        }





      /*  if (swap == "red"){
            MeshRenderer meshRenderer = obj1.GetComponent<MeshRenderer>();
            meshRenderer.material = newMaterial1;


        }
        else if (swap == "green")
        {
            MeshRenderer meshRenderer = obj2.GetComponent<MeshRenderer>();
            meshRenderer.material = newMaterial2;
        }
  
        else
        {
           Debug.Log("noting ");
        }*/
    }




}
