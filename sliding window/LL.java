import java.util.Scanner;

public class LL{
    private node head;
    private node tail;
    private int size;
    LL(){
        this.size=0;
        this.head=null;
        this.tail=null;

    }
        private class node{
        private int value;
        private node next;
        node(int value){
            this.next=null;
            this.value=value;
        }
        node(int value,node next){
            this.next=next;
            this.value=value;
        }
        }
    
    public void insertfirst(int value){
        node n=new node(value);
        n.next =this.head;
        this.head=n;
        if (tail==null){
            tail=this.head;
        }
        size+=1;
    }
    public void insertlast(int value){
        if(this.tail==null){
            this.insertfirst(value);
            return;
        }
        node n=new node(value);
        this.tail.next=n;
        this.tail=n;
        size++;
    }
    public void insert(int val,int index){
        if (index==0){
            this.insertfirst(val);
            return;
        }
        if (index==size){
            this.insertlast(val);
        }
        node temp=this.head;
        for(int i=0;i<index-1;i++){
            temp=temp.next;
        }
        node n=new node(val,temp.next);
        temp.next=n;
        size++;

    }

    public int deletefirst(){
        int n=head.value;
        head=head.next;
        if(head==null){
            tail=null;
        }size--;
        return n;
    }
    //return index node
    public node get(int index){
        node n=head
        if(n<0 || n>size){
            System.out.println("enter valid number");
            return null;
        }
        for(int i=0;i<index;i++){
            n=n.next;
        }
        return n;
    }

    public int deletelast(){
        if(size<2){
            deletefirst();
            return;
        }
        node secn=get(size-2);
        int n=tail.value;
        size--;
        secn.next=null;
        tail=secn;
        return n;

    }
    public int delete(int index){
        if(index==0){deletefirst();return;}
        if(index==size-1){
            deletelast();
            return;
        }
        if(index<0 || index>=size){
            System.out.println("not possible");
            return;
        }
        node n=get(index-1);
        int n=n.next.value;
        n.next=n.next.next;
        size--;
        return n;
    }

    //search an element
    public node find(int val){
        node temp=head;
        while(temp!=null){
            if(temp.value==val){
                return temp;
            }temp=temp.next;
        }return null;
    }
    public void display(){
        node temp=this.head;
        if(this.head==null){
            System.out.println("list is empty");
        return;}
        System.out.println("the link:");
        do{
        System.out.println(temp.value);
        temp=temp.next;
        }while(temp.next!=null);
        // System.out.println(temp.value);
    }
    public void removeduplicates(){
        node n=head;
        while(n.next!=null){
            if(n.value==n.next.value){
                n.next=n.next.next;
                size--;
            }else{
                n=n.next
            }
        }
    }

    

    public static void main(String a[]){
        System.out.println("1->insert first");
        System.out.println("2->insert last");
        System.out.println("3->insert at position");
        System.out.println("4->Display all");
        // System.out.println("1->insert first");
        // System.out.println("1->insert first");
        Scanner in =new Scanner(System.in);
        LL ll =new LL();
        int ch,val,pos;
        do{ 
            System.out.print("Enter option:");
            ch=in.nextInt();
            switch(ch){
            case 1:
                System.out.print("enter value:");
                val=in.nextInt();
                ll.insertfirst(val);
                break;
            case 2:
                System.out.print("enter value:");
                val=in.nextInt();
                ll.insertlast(val);
                break;
            case 3:
                System.out.println("enter value and pos:");
                val=in.nextInt();
                pos=in.nextInt();
                ll.insert(val,pos);
                break;
            case 4:
                ll.display();
                break;
            case 5:
                break;
            default:
            System.err.println("error");
        }}while(ch!=5);
        in.close();
    }
}