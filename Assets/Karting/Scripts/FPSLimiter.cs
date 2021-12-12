using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FPSLimiter : MonoBehaviour

{
    public int frameRate = 40;
    // Start is called before the first frame update
    void Start()
    {
        Application.targetFrameRate = frameRate;
    }

 
}
