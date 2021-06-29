import java.util.*; 
import java.io.*; 
import java.util.Comparator;

class Hackathon {
    String name;
    int dd, mm, yy;

    Hackathon(String name, int dd, int mm, int yy) {
        this.name = name;
        this.dd = dd;
        this.mm = mm;
        this.yy = yy;
    }

}

class NameComparator implements Comparator {  
    public int compare(Object a, Object b){  
        Hackathon h1 = (Hackathon) a;  
        Hackathon h2 = (Hackathon) b;  
        
        return (h1.name).compareTo(h2.name);  
    }
} 

class DateComparator implements Comparator {  
    public int compare(Object a, Object b){  
        Hackathon h1 = (Hackathon) a;  
        Hackathon h2 = (Hackathon) b;    
    
        if (h1.yy <= h2.yy && h1.mm <= h2.mm && h1.dd <= h2.dd)  
            return 1;   
        else  
            return -1;  
        }  
}  
 
  
class SortHackathons{  
    public static void main(String args[]){  
    
        ArrayList <Hackathon> mlh_hackathons = new ArrayList();  
        mlh_hackathons.add(new Hackathon("Pride Hacks", 10, 2, 20));  
        mlh_hackathons.add(new Hackathon("Hack the Mountains", 1, 12, 19)); 
        mlh_hackathons.add(new Hackathon("HackItshipIt", 17, 7, 21));
        mlh_hackathons.add(new Hackathon("Hacky Birthday MLH", 21, 7, 21));
        mlh_hackathons.add(new Hackathon("Sun hacks", 2, 9, 21));  
        
        System.out.println("Sorting by Name\n");  
        
        Collections.sort(mlh_hackathons,new NameComparator());  
        Iterator itr = mlh_hackathons.iterator();  
        while(itr.hasNext()){  
            Hackathon st = (Hackathon)itr.next();  
            System.out.println(st.name+" "+st.dd + " " + st.mm + " " + st.yy);  
        }  
        
        System.out.println("\nSorting by date\n");  
        
        Collections.sort(mlh_hackathons,new DateComparator());  
        Iterator itr2 = mlh_hackathons.iterator();  
        while(itr2.hasNext()){  
            Hackathon st = (Hackathon)itr2.next();  
            System.out.println(st.name+" "+st.dd + " " + st.mm + " " + st.yy);  
        } 
    }  
} 

