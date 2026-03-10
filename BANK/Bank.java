package BANK;
class Account {

    public String name;
    protected String email;
    private String password;

    public String getPasss() {
        return this.password;
    }

    ;
    public void setPass(String pass) {
        this.password = pass;
    }
}
public class Bank {
    public static void main(String[] args) {
        Account account1 = new Account();
        account1.name = "Yash GUpta";
        account1.email = "yash@hkbd";
        account1.setPass("yash");
        System.out.println(account1.getPasss());
    }
}