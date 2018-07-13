package ml

import scala.util.{Try, Success, Failure}
import java.io._

object Label extends App{
  
  def readTextFileWithTry(filename: String): Try[List[String]] = {
    Try {
        val lines = using(io.Source.fromFile(filename)) { source =>
            (for (line <- source.getLines) yield line).toList
        }
        lines
    }
    
  }
  
  val passwdFile = readTextFileWithTry("test.txt")
  val pw = new PrintWriter(new File("output.txt" ))
  passwdFile match {
      case Success(lines) => lines.foreach{ str =>
        str.toInt match {
          case str if 0 until 25 contains str => pw.println("average")
          case str if 25 until 50 contains str => pw.println("high")
          case unknow  => println("Others")
      } 
  }
      case Failure(s) => println(s"Failed, message is: $s")
  }

  pw.close()
  
   def using[A <: { def close(): Unit }, B](resource: A)(f: A => B): B =
        try {
            f(resource)
        } finally {
            resource.close()
    }
}