import java.util.*;

class bst{
static class Node{
int data;
Node left;
Node right;
Node(int data){
this.data=data;
this.left=this.right=null;
}}

public static Node search(Node root,int key){
if(root==null||root.data==key){return root;}
if(root.data>key){return search(root.left,key);}
if(root.data<=key){return search(root.right,key);}
return null;
}

public static Node insert(int data,Node root){
if(root==null){
return new Node(data);
}
if(root.data>data){root.left= insert(data,root.left);}
else if(root.data<=data){root.right= insert(data,root.right);}
return root;
}

public static void lvlorder(Node root){
if(root==null){return;}
Queue<Node> q=new LinkedList<>();
q.add(root);
while(!q.isEmpty()){
int s=q.size();
for(int i=0;i<s;i++){
Node curr=q.remove();
System.out.print(curr.data+" ");
if(curr.left!=null){q.add(curr.left);}
if(curr.right!=null){q.add(curr.right);}
}
System.out.println();
}
}

public static Node delete(Node root,int key){
Node deln=null;
if(root==null) return null;
if(key<root.data) return delete(root.left,key);
else if(key>root.data) return delete(root.right,key);
else{
deln=root;
if(root.left==null)root= root.right;
else if(root.right==null)root=root.left;
else{
Node minvalsuc=successor(root.right);
root=minvalsuc;
delete(root.right,minvalsuc.data);
}
}
return deln;
}
public static Node successor(Node root){
while(root.left!=null)root=root.left;
return root;
}
public static void main(String a[]){
Node root=null;
root=insert(5,root);
root=insert(3,root);
root=insert(7,root);
root=insert(1,root);
root=insert(4,root);
root=insert(6,root);
root=insert(8,root); 
lvlorder(root);
delete(root,3);
lvlorder(root);
System.out.println(search(root,4).data);
}
}
