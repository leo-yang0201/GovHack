package geoJson;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;

public class WriteToTxt {
	//将读取的关键词写入记事本
	public static void contentToTxt(String filePath, String content) {
        try{
            BufferedWriter writer = new BufferedWriter(new FileWriter(new File(filePath),true));
            writer.write(content);
            writer.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
