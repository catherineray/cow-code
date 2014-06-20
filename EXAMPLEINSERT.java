public class EXAMPLEINSERT {



  public static void insertIntoTable(String jdbcURL, String USER, String PASS) {



    Connection conn = null;

    Statement stmt = null;

    // add Prepared statement outside of try-catch

    PreparedStatement prepareStatement = null;

    try{

        // Open a connection

        conn = DriverManager.getConnection(jdbcURL, USER, PASS);

      

        // Execute insert

        stmt = conn.createStatement();

        String tableName = "TABLENAME";



        // Avoid temptation and deliver yourself from the evils of coding Java as if it were Python.

        String template = "INSERT INTO” + tableName + “ (name, field, university, alive) VALUES (?, ?, ?, ?)";



        statement = conn.prepareStatement(template);

        statement.setString(1, name);

        statement.setString(2, field);

        statement.setString(3, university);                     

        statement.setBoolean(4, alive);



        statement.executeUpdate();

        //More hardcoding? Slightly, but also more robust.

    }

    conn.close();

    } catch(Exception e) {

      System.err.println(e.getMessage());

    }

  }

}