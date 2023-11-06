using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class screenshot : MonoBehaviour
{
    public Camera arCamera;

    public void OnCaptureButtonClick()
    {
        // Set the render texture to the camera's target texture
        RenderTexture.active = arCamera.targetTexture;

        // Create a new texture to hold the captured image
        Texture2D texture = new Texture2D(arCamera.targetTexture.width, arCamera.targetTexture.height, TextureFormat.RGB24, false);

        // Read the pixels from the render texture into the texture
        texture.ReadPixels(new Rect(0, 0, arCamera.targetTexture.width, arCamera.targetTexture.height), 0, 0);
        texture.Apply();

        // Save the texture to a file
        byte[] bytes = texture.EncodeToPNG();
        string filename = "screenshot.png";
        File.WriteAllBytes(filename, bytes);

        // Reset the render texture
        RenderTexture.active = null;
    }
}